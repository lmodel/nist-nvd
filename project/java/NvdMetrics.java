package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The scores of a vulnerability, in a list per scoring system and version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdMetrics  {

  private List<NvdCvssMetricV40> cvssMetricV40;
  private List<NvdCvssMetricV31> cvssMetricV31;
  private List<NvdCvssMetricV30> cvssMetricV30;
  private List<NvdCvssMetricV2> cvssMetricV2;
  private List<NvdSsvcMetricV203> ssvcV203;


}