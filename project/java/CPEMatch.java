package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Leaf-level CPE match criterion and optional version bounds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CPEMatch  {

  private String matchCriteriaId;
  private String criteria;
  private String cpe23Uri;
  private boolean vulnerable;
  private String versionStartIncluding;
  private String versionStartExcluding;
  private String versionEndIncluding;
  private String versionEndExcluding;
  private List<String> matchedCpeNames;

}